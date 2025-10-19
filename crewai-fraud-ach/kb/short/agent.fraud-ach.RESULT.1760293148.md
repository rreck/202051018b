```json
{
  "id": "2982efffbec35471",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293148,
  "host_pid": "9e6742732c60:1",
  "hash": "ac18ef3b1836bd08451537b8b0dfadb189ff642457d1d059e90e72ce48b27ede",
  "cid": "QmV1ac18ef3b1836bd08451537b8b0dfadb189ff6424",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293148,
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
      "evaluated_at": 1760293148
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
  "sig": "d671cd602bd65ce8cad6d00f978e300d628236950e49c483c710a959e42578e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275925775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 41077756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': 'faef3b4bfd0d33cd'}}}