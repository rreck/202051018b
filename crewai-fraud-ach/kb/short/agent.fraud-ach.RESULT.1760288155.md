```json
{
  "id": "0068f6e51914b5a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288155,
  "host_pid": "9e6742732c60:1",
  "hash": "07c93c48257b1db7d529914b997a92f9f5aa30faa4831003c69d4d358786d885",
  "cid": "QmV107c93c48257b1db7d529914b997a92f9f5aa30fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288155,
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
      "evaluated_at": 1760288155
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
  "sig": "36d754b206198bba940393abdfd0039fbb50a0b03d166edc52e125e72ad946d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026828395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': '40ce51f53058bb71'}}}