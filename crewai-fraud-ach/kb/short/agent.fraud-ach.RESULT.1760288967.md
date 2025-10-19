```json
{
  "id": "5452cfd4e6508dfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288967,
  "host_pid": "9e6742732c60:1",
  "hash": "6bbe1ef0e37245412df288ccdabd7a46403e7cdfca339b5b9578d0dff8861d00",
  "cid": "QmV16bbe1ef0e37245412df288ccdabd7a46403e7cdf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288967,
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
      "evaluated_at": 1760288967
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
  "sig": "196154c0e4d2cd1a26c9b4959559dda3cdd7fe4a762e5b900a88aa3a1fc5e06b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021597485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 29412778, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': '53d96e948794c738'}}}