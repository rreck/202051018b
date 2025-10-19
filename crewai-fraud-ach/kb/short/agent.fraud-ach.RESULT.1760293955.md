```json
{
  "id": "c9315332e7c864e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293955,
  "host_pid": "9e6742732c60:1",
  "hash": "62ae532fcd1486d82ce2f09aa4ec9608df4d500efc70aa432e8dbccd329bc3d1",
  "cid": "QmV162ae532fcd1486d82ce2f09aa4ec9608df4d500e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293955,
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
      "evaluated_at": 1760293955
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
  "sig": "bcbe1b324ac8d8082f313c3647faacf2f6db4e09a7249a625a895754f564fab9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034128514
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 46270137, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '342851cb36b9daae'}}}