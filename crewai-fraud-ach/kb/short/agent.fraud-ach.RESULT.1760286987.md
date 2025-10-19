```json
{
  "id": "73612b05189216bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286987,
  "host_pid": "9e6742732c60:1",
  "hash": "89ad502e280dc77fe4ceb7614c34f9ac444f4b754f66f94787a548b166643752",
  "cid": "QmV189ad502e280dc77fe4ceb7614c34f9ac444f4b75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286987,
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
      "evaluated_at": 1760286987
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8ba10182f5da780862b07ad9fa7b24158c056df57e402d9d627c6bc950f8e443"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000027064013
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13095896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285765, 'matching_hash': '811cb7a859f68158'}}}