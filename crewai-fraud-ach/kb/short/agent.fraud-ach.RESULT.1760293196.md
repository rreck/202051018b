```json
{
  "id": "ffd5a70723131997",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293196,
  "host_pid": "9e6742732c60:1",
  "hash": "147a85e9b65bf6d1835c8d617c89f2ed41bc07612f18fab9c7de101e4b95f7d0",
  "cid": "QmV1147a85e9b65bf6d1835c8d617c89f2ed41bc0761",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293196,
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
      "evaluated_at": 1760293196
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
  "sig": "c2418644d5dc3ceb5686692920694c69c591da7b2e91451feae8e71672255282"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469007601
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 21560286, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}