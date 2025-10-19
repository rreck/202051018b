```json
{
  "id": "3cbe769219a2b2f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294145,
  "host_pid": "9e6742732c60:1",
  "hash": "7593c8e3c161cb05251ec777a5210b1407cf14942c3c5e569c6461171a059a31",
  "cid": "QmV17593c8e3c161cb05251ec777a5210b1407cf1494",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294145,
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
      "evaluated_at": 1760294145
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
  "sig": "f43968dac3b4a9b8b0ff3fcf74505e001523a9cdcc57e6cc9a01b5544966bc10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 47340992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}