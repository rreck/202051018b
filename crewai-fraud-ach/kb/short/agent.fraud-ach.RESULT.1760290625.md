```json
{
  "id": "4b97ceb62fba62b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290625,
  "host_pid": "9e6742732c60:1",
  "hash": "cbd9e2fd88961c5492aee2220c3a051148f21c2bd968b50d6651f335e452c041",
  "cid": "QmV1cbd9e2fd88961c5492aee2220c3a051148f21c2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290625,
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
      "evaluated_at": 1760290625
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
  "sig": "5dfa4fb0c5292f019d3c1606a2dc9a710a1f7f0619c5f967093f5a676bd4b53d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 77039960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}