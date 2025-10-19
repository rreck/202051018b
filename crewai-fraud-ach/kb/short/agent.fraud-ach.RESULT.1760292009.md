```json
{
  "id": "1799ff42128d0619",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292009,
  "host_pid": "9e6742732c60:1",
  "hash": "394eac82aaae4e99e8804aeddb76738f09ca138530add6a5e205875697fe82f6",
  "cid": "QmV1394eac82aaae4e99e8804aeddb76738f09ca1385",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292009,
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
      "evaluated_at": 1760292009
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
  "sig": "5bed13fe05679996ae544cc5fcbb2f443bf837b6e1babb7dbcd4fc37b74ed729"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027737863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 88487464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285764, 'matching_hash': '0d7de9a99f2e5847'}}}