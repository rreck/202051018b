```json
{
  "id": "19d4b03f54416164",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286001,
  "host_pid": "9e6742732c60:1",
  "hash": "f83cf656c4c8eb9eab898933ac4f975f351062fc97b8ba19e54c1a1fe22cff3b",
  "cid": "QmV1f83cf656c4c8eb9eab898933ac4f975f351062fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286001,
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
      "evaluated_at": 1760286001
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
  "sig": "abe677bccb6e89a9e5f3f5dc93fa1b47aef100b39c20d03991034b254ca5c91b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156493582
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285763, 'matching_hash': '28d5522bb9de7370'}}}