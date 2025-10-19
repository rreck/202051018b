```json
{
  "id": "4b66ab2598997f57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288036,
  "host_pid": "9e6742732c60:1",
  "hash": "2b7c69218d30e22595176c400a51f793a02fc1b0010e65e51a13de2b4be00da3",
  "cid": "QmV12b7c69218d30e22595176c400a51f793a02fc1b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288036,
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
      "evaluated_at": 1760288036
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
  "sig": "00846be410dec8786f74e23947e2643047e6e958c2a078f651b4cf0cdc58bf53"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 25459840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}