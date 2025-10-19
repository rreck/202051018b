```json
{
  "id": "8d34ea17f80ca2b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288207,
  "host_pid": "9e6742732c60:1",
  "hash": "3e79fc77c293b70cfeb9ae86d7fa1b95701c482f980b62ff3921cf182aa49908",
  "cid": "QmV13e79fc77c293b70cfeb9ae86d7fa1b95701c482f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288207,
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
      "evaluated_at": 1760288207
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "fa4115241ca6ff7e1ba1b933a304cdc1e01712fe9f27d333db15c4334d8a8781"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 886156735269080
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 16494886, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285765, 'matching_hash': 'bf20bb751245cb05'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '886156735', 'validation_error': 'Invalid routing number checksum'}}}