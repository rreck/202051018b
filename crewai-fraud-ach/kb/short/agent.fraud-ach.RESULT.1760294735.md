```json
{
  "id": "350b0d0604e712d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294735,
  "host_pid": "9e6742732c60:1",
  "hash": "518cfa11ca9057d05b6eaafdbfb97d6c630ef5d78bb8cf145d5c8bedea874323",
  "cid": "QmV1518cfa11ca9057d05b6eaafdbfb97d6c630ef5d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294735,
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
      "evaluated_at": 1760294735
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
  "sig": "acbb0d2a68f79532b5432db29493eb5aa5dc6de55d589fec9426c26270ffca70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153937190
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 117785259, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': '8cf441fb6328957e'}}}