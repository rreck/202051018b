```json
{
  "id": "9542235a774b23aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289806,
  "host_pid": "9e6742732c60:1",
  "hash": "42b46a0de3726b2cd12c761e8c320c661ea58628f205eeca6281059fc6219eae",
  "cid": "QmV142b46a0de3726b2cd12c761e8c320c661ea58628",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289806,
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
      "evaluated_at": 1760289806
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
  "sig": "72964f3f929e8115128ebea39e82da87e3a1a96b15bd9818e80cdf57dbe87347"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 42326984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}