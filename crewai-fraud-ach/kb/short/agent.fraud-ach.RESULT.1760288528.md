```json
{
  "id": "0be62988f6361d16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288528,
  "host_pid": "9e6742732c60:1",
  "hash": "e8035c51a6d4fe6d80a197facc43ae698bd336386c928677c9f32dd6beb8e877",
  "cid": "QmV1e8035c51a6d4fe6d80a197facc43ae698bd33638",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288528,
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
      "evaluated_at": 1760288528
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
  "sig": "982660272cb93e3e121661a59015df1f089133cba3a591df9328a1d29fe2fa58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596855798
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 25355904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': 'aef06f437446325c'}}}