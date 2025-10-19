```json
{
  "id": "aa5b015031cd0d9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289578,
  "host_pid": "9e6742732c60:1",
  "hash": "402cfc78dcc6bd4d2203b2b1377b2163434463de8d345f9f7eb2ef6a84e15569",
  "cid": "QmV1402cfc78dcc6bd4d2203b2b1377b2163434463de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289578,
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
      "evaluated_at": 1760289578
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
  "sig": "cc5511e990a412d0827896e3e7542c8bb4737092d49b730768f16123af1c0d20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274446776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 39831518, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': '03cceccb7405bcab'}}}