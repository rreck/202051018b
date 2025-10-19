```json
{
  "id": "5590f43f8f147c73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293587,
  "host_pid": "9e6742732c60:1",
  "hash": "53f04d699f2098d0cd9073ee194318b8ee5119de5d757a7e57f3c6e588053472",
  "cid": "QmV153f04d699f2098d0cd9073ee194318b8ee5119de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293587,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293587
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "1be4b5605fffaaa034d23adfb4f3b5c15c80d76c7019ed33f643e6fba71dd695"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466322331
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 19968897, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': '8006c6780242cc6a'}}}