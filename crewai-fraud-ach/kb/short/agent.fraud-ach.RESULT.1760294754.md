```json
{
  "id": "83af409f326c19cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294754,
  "host_pid": "9e6742732c60:1",
  "hash": "d0eb6d849bb5843bcf7a2acf04cc6db35927c6971b93d6d0cbdba611dff89ccf",
  "cid": "QmV1d0eb6d849bb5843bcf7a2acf04cc6db35927c697",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294754,
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
      "evaluated_at": 1760294754
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
  "sig": "8f2c26a748fd6e60723f926b0695ab6b3e355bc416fa8a4927e613073a30cd0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157097598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 78055600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '62fa124f01b3075a'}}}