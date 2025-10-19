```json
{
  "id": "1653ca968883020e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292333,
  "host_pid": "9e6742732c60:1",
  "hash": "66044dcd3b26e793e7719b5e01a04c8ea2bdd0b90d759d88c06f858caa75cf8b",
  "cid": "QmV166044dcd3b26e793e7719b5e01a04c8ea2bdd0b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292333,
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
      "evaluated_at": 1760292333
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
  "sig": "31b6883181017a3a56958255d25ad5acdc044903c75143d48d0de8cde6dd4ce3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243386632
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 43251975, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'a6aa6f7765b452ca'}}}