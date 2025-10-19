```json
{
  "id": "3978d24d757ff073",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289952,
  "host_pid": "9e6742732c60:1",
  "hash": "4e6c8b6b5bcdd9483e04e2fbade22ef734251b4065d24487d3ccf25ee5bfc8b6",
  "cid": "QmV14e6c8b6b5bcdd9483e04e2fbade22ef734251b40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289952,
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
      "evaluated_at": 1760289952
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
  "sig": "1c16abb2bec52a6bfbd6607cf51b9c807f76e264d123275fb55f3ddb6c8e3ead"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274128098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 56829792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285765, 'matching_hash': 'e67ed82943972fb3'}}}