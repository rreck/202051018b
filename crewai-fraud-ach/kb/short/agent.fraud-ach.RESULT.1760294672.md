```json
{
  "id": "7b2effcb76a00fa4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294672,
  "host_pid": "9e6742732c60:1",
  "hash": "1a3c1534f39f40030773a41757f6f7fd264f2a649eb0e126b8ec9145868b8fae",
  "cid": "QmV11a3c1534f39f40030773a41757f6f7fd264f2a64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294672,
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
      "evaluated_at": 1760294672
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
  "sig": "f8ed7d228970cf5cd85b0f1172f90fd5ad65241d4d66e056fc63b5e0e863bfe9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023479394
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 95148592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '601e7e272d8441f2'}}}