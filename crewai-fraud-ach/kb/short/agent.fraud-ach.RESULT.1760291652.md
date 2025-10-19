```json
{
  "id": "e0ab40437a4e5ae7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291652,
  "host_pid": "9e6742732c60:1",
  "hash": "2522170c97483632f318b36a405b7df7ef9d9699c5cfe9f8538d6a77cc3acfd8",
  "cid": "QmV12522170c97483632f318b36a405b7df7ef9d9699",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291652,
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
      "evaluated_at": 1760291652
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
  "sig": "926e5c3485ac2026cdbfdee8ed35b4a2fd95a030f3449ec66b2b70ec114fe0e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020641018
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 29108160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '9cb08faa1a3d5c0e'}}}