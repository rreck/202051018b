```json
{
  "id": "3d67ce7f7e19d3e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290580,
  "host_pid": "9e6742732c60:1",
  "hash": "5776c4ef7fc4062c4b012ca4faaf2bb4002581c5b95c191e5bffd71dfe4ffec8",
  "cid": "QmV15776c4ef7fc4062c4b012ca4faaf2bb4002581c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290580,
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
      "evaluated_at": 1760290580
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
  "sig": "44cd75ced79c1e2f6489752fe5f91cd0fabe54e167183c0e61a72615a42535a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249268740
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 11948244, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': '2b1c4c9f55d7dd69'}}}