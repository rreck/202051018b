```json
{
  "id": "ab8090a6f889a1ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290112,
  "host_pid": "9e6742732c60:1",
  "hash": "1efa5329ea46383c46bc503aa25527c32232d0f4d8061e2ee24d2b590a53e4d1",
  "cid": "QmV11efa5329ea46383c46bc503aa25527c32232d0f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290112,
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
      "evaluated_at": 1760290113
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
  "sig": "4756410877221f35c4a34720bea2eea9867a4cd218225f40aa50b75821bfed16"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155806195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 33536566, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': '37264973f9c39fe3'}}}