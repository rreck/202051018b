```json
{
  "id": "71ad411c89d57047",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290514,
  "host_pid": "9e6742732c60:1",
  "hash": "460fea20a24e04d5e25497dd737d38ad8f3a16b02d7b622ac27c933b1dee2d53",
  "cid": "QmV1460fea20a24e04d5e25497dd737d38ad8f3a16b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290514,
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
      "evaluated_at": 1760290514
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
  "sig": "acffe0f664f242d873105bb83eb8d8b82885e636c820afda80387b73863f7d62"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270534223
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 27233536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '6dd341e8ae885101'}}}