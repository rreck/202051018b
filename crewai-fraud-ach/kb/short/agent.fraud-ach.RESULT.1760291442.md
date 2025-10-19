```json
{
  "id": "b4c26fa04aa09fc7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291442,
  "host_pid": "9e6742732c60:1",
  "hash": "8c67379050ed7f114c5883c6f823b0629509a37e2881e52e2e729c1a8a9f94de",
  "cid": "QmV18c67379050ed7f114c5883c6f823b0629509a37e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291442,
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
      "evaluated_at": 1760291442
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
  "sig": "bf917a4432df54963dc355282c3e2f49189766375c67a5c6e213329c0e87ca1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592967123
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 30847600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': 'c09be009c43e6bc8'}}}