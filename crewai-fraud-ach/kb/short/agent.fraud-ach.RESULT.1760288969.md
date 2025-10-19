```json
{
  "id": "7b9ff84286c19eaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288969,
  "host_pid": "9e6742732c60:1",
  "hash": "b49185773e9823630d87b0715222d327fccb8ae97cf81d0e0f43529e8517d3fa",
  "cid": "QmV1b49185773e9823630d87b0715222d327fccb8ae9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288969,
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
      "evaluated_at": 1760288969
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
  "sig": "f46239084ad5ca94829b7576ffeca71235b7b495010eefdfeb2d0fecf15014ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 34689032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}