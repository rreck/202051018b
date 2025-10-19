```json
{
  "id": "7404c3585307cf41",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294498,
  "host_pid": "9e6742732c60:1",
  "hash": "41d6b6d92eeb971f47414ff9f5d429050e9ec71638b16255e635c2ea4b360e33",
  "cid": "QmV141d6b6d92eeb971f47414ff9f5d429050e9ec716",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294498,
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
      "evaluated_at": 1760294499
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
  "sig": "040fd414168335d62f2eccaa4461f49c644fc12216363fddb30e8dadbee7ae94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596367142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 108281818, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '4f1a5a8d43b99e0b'}}}