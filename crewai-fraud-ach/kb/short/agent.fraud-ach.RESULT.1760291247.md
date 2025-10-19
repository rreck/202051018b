```json
{
  "id": "8c1bb0098a20210b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291247,
  "host_pid": "9e6742732c60:1",
  "hash": "c25ea9896ce613467f36e654bd7e98ff030ec20c6574bb96ada19a822074f498",
  "cid": "QmV1c25ea9896ce613467f36e654bd7e98ff030ec20c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291247,
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
      "evaluated_at": 1760291247
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
  "sig": "f239109ceeebbbd4e4b66365f0e939669df645f1596422bb35779e48a3cd5b3f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712851
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 14139920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285765, 'matching_hash': 'f72222764ca627d0'}}}