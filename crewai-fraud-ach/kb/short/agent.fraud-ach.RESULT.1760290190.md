```json
{
  "id": "67464b0df5c742b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290190,
  "host_pid": "9e6742732c60:1",
  "hash": "c16dff85532094a45aac513cbe46f5c461f9166b12c695cb9468b5b28a894e3a",
  "cid": "QmV1c16dff85532094a45aac513cbe46f5c461f9166b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290190,
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
      "evaluated_at": 1760290190
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
  "sig": "d7b364dee2b53feaab820c145fd840e6d36e3b4228570e489f35eea4ebf805f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590857246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 51034464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': 'f091f96bdb04a5bf'}}}