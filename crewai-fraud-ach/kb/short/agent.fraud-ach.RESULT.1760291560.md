```json
{
  "id": "26a99b067cc59732",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291560,
  "host_pid": "9e6742732c60:1",
  "hash": "046fe7493b4a4bfdecc168eb8986478624eb25898fb4d68ec50e51ab76add222",
  "cid": "QmV1046fe7493b4a4bfdecc168eb8986478624eb2589",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291560,
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
      "evaluated_at": 1760291560
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
  "sig": "ee3000f828cbf43e3771c847439384e234035fd2186e30142b701ceb76c2c784"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270864889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 33839402, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': 'c03eacc7eaf45e0d'}}}