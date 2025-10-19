```json
{
  "id": "cdd6f311ed260bf6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288159,
  "host_pid": "9e6742732c60:1",
  "hash": "0e73155ae528b865d529584664b0f16afc804c48d1abc3fa3b1e7b3c0fb76197",
  "cid": "QmV10e73155ae528b865d529584664b0f16afc804c48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288159,
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
      "evaluated_at": 1760288159
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
  "sig": "63d9cd6d9a7995098f754897b33eedb5d601c15e0a6ed0e027f59ddfa9051c70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026265735
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 29575392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': 'e94388ee515b2db1'}}}