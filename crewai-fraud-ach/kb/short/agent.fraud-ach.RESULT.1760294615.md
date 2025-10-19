```json
{
  "id": "63faee48cf05efac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294615,
  "host_pid": "9e6742732c60:1",
  "hash": "92b394676f844ec35706910c8b6e9ae2a67076e1214c3b0a87cba9153ee06683",
  "cid": "QmV192b394676f844ec35706910c8b6e9ae2a67076e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294615,
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
      "evaluated_at": 1760294615
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
  "sig": "5cb64998f2c0972ff63a8aaefde2299e6729cecae347e617eac8ca957756fdea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039215537
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 58223190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': '4decba5555bb1e33'}}}}