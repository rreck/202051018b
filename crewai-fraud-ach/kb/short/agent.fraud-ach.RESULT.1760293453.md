```json
{
  "id": "5e1d72eb0ce4c93e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293453,
  "host_pid": "9e6742732c60:1",
  "hash": "a57c57851e8b0e15c8fca4f33217c8ef8ef4c6bfdeb9819ce38293c4f84536e9",
  "cid": "QmV1a57c57851e8b0e15c8fca4f33217c8ef8ef4c6bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293453,
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
      "evaluated_at": 1760293453
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
  "sig": "3d3afe1743b4f590cae1dc3bc6df54317645a2f103c38c6ca56d4754a6e9ee81"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591082294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 101716959, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': 'b890dc886075e9be'}}}