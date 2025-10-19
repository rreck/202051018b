```json
{
  "id": "03ce3486f5b69067",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288761,
  "host_pid": "9e6742732c60:1",
  "hash": "260c2473e22f2b4117b8e77c4b404537a425d38a5574010c9225ac38497d24ef",
  "cid": "QmV1260c2473e22f2b4117b8e77c4b404537a425d38a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288761,
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
      "evaluated_at": 1760288761
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
  "sig": "abac0f59cf95c3206635ceed792b38d1131dbb5ddb3592b48a0130450f46c6bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467837924
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 10189893, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': '256da828ea708baa'}}}