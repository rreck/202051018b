```json
{
  "id": "0ba3e280dc243288",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293489,
  "host_pid": "9e6742732c60:1",
  "hash": "c13d89a1a7f80d14e1f24197c3c8ae7fc5d7504ad775fc146e59bec859ddf7b1",
  "cid": "QmV1c13d89a1a7f80d14e1f24197c3c8ae7fc5d7504a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293489,
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
      "evaluated_at": 1760293489
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
  "sig": "8692d7d23099cdfc04aa626ed0e35c4ff0b79b33196ffa96ebea02bd2c0734c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 84367560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': '7a1c6367235ff38a'}}}