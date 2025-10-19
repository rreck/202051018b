```json
{
  "id": "5dc01436445bdab3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287274,
  "host_pid": "9e6742732c60:1",
  "hash": "3065ed8d6a6c8977ddd84e1a8a85e2aa49167e00c0dbcfc767004f9268f7fe1a",
  "cid": "QmV13065ed8d6a6c8977ddd84e1a8a85e2aa49167e00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287274,
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
      "evaluated_at": 1760287274
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "08e2265ef8a12950b66b0d9674020cf38076884a2ef4e16d72bca14377e5890f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000029441717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 11492172, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285764, 'matching_hash': 'f6bac04718607b3a'}}}