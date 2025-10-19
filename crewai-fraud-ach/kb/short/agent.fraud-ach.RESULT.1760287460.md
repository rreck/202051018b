```json
{
  "id": "87e6ed6d1fa3439b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287460,
  "host_pid": "9e6742732c60:1",
  "hash": "c116d93567a060e42db40034d0ca2d1e95d16ad6ef27fad4cd4f186ecf07ecfa",
  "cid": "QmV1c116d93567a060e42db40034d0ca2d1e95d16ad6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287460,
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
      "evaluated_at": 1760287460
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
  "sig": "8423bdd78f5b6408f3ec5a438c25008f77e1bc503b404fbc11ab3a49cf940e13"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 026009596329202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 10612780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285763, 'matching_hash': 'fa5bd443d3b1bd8d'}}}