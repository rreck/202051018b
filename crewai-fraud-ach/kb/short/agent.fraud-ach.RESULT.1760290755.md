```json
{
  "id": "3046e6ab84b09039",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290755,
  "host_pid": "9e6742732c60:1",
  "hash": "cb2df6288e42461073a95b64be49437aba187eed5dbce28d122d417e1d4efd64",
  "cid": "QmV1cb2df6288e42461073a95b64be49437aba187eed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290755,
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
      "evaluated_at": 1760290755
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
  "sig": "4537e2ba3d6a1d3074e6173982850f2f780bf785511a5296b100a23371268eee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029278927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 45657892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}