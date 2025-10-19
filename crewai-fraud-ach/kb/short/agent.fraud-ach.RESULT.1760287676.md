```json
{
  "id": "81ac4638fe605368",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287676,
  "host_pid": "9e6742732c60:1",
  "hash": "1d08dda56bf0a4d0c51c0ae9b84ae51372a48864df092b9ed95c2314ec6c3902",
  "cid": "QmV11d08dda56bf0a4d0c51c0ae9b84ae51372a48864",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287676,
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
      "evaluated_at": 1760287676
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
  "sig": "fdf22534a7db375c377e9e335d55490aa250e5d3be9757677c5389970180c460"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 21640864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}