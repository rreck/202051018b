```json
{
  "id": "b799e83b40a9d153",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289830,
  "host_pid": "9e6742732c60:1",
  "hash": "51a0eb6511a20d7b0326c99bb0d1b80e96517572ce9ad19e05f1cc79408b9823",
  "cid": "QmV151a0eb6511a20d7b0326c99bb0d1b80e96517572",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289830,
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
      "evaluated_at": 1760289830
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
  "sig": "d24ff749a6ba784020b85c79de45f64ec5f4991a674e6e7aa8dd326269924bb0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279768309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 17506650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760284979, 'matching_hash': '8798983dc5a8227d'}}}