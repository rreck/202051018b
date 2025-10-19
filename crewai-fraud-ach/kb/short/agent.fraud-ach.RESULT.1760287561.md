```json
{
  "id": "7502769368d8aa55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287561,
  "host_pid": "9e6742732c60:1",
  "hash": "27f2bfc2d34cf251722a01e794c3bffafbf417f12fabd342e729021faed0a928",
  "cid": "QmV127f2bfc2d34cf251722a01e794c3bffafbf417f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287561,
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
      "evaluated_at": 1760287561
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
  "sig": "b2a394ddd406814b6d9edc06133316e6a63fbfd04f99cd8c07b9e90706fd12cf"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 20367872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}