```json
{
  "id": "e40b7aed9cb93d96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290153,
  "host_pid": "9e6742732c60:1",
  "hash": "95b9e16c7783fdb6ae3f76f2e78cf19f3a04f0d03df04cffa779d6820c29991b",
  "cid": "QmV195b9e16c7783fdb6ae3f76f2e78cf19f3a04f0d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290153,
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
      "evaluated_at": 1760290153
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
  "sig": "6004be75b8be0d6c7379b3d789c4a9c7a21b817052838f650fcf7a6214528238"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029133644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 69571502, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': 'fa9b9676ccddb30b'}}}