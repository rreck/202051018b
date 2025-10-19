```json
{
  "id": "28bfe79b091df3b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287780,
  "host_pid": "9e6742732c60:1",
  "hash": "9c94da46228d783351f1242f61748f30e360dd37e0860e81e48642d09d66e78e",
  "cid": "QmV19c94da46228d783351f1242f61748f30e360dd37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287780,
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
      "evaluated_at": 1760287780
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
  "sig": "9f3e13408b69e6f399de60548fd28bef135c1ca322377d2881deedb88d007659"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 026009596636125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 32060304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': 'de29ac64387e8e3f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '886156735', 'validation_error': 'Invalid routing number checksum'}}}