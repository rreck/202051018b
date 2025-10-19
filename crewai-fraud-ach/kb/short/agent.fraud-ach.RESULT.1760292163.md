```json
{
  "id": "388bc0a032f665f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292163,
  "host_pid": "9e6742732c60:1",
  "hash": "5d8c683101c7c0b18497c6758eb9770263afa5cd57aef04d08cf487375ab9d92",
  "cid": "QmV15d8c683101c7c0b18497c6758eb9770263afa5cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292163,
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
      "evaluated_at": 1760292163
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
  "sig": "e50bd892f7694c3d5b6b207c065ebe6c08f2f3316a29a166002be3bf0a25ffec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 60785368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}