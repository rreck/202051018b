```json
{
  "id": "bcd4669a264db5ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293680,
  "host_pid": "9e6742732c60:1",
  "hash": "6267c90d80f11c9a4cb5cace222b251ecaa6fcf2b9ae0408633bd6ffa17626b9",
  "cid": "QmV16267c90d80f11c9a4cb5cace222b251ecaa6fcf2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293680,
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
      "evaluated_at": 1760293680
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
  "sig": "083c4251ec807a216505471b564348cef75f12c7eec7405c5fa9d99826d8de6b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 105356350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}