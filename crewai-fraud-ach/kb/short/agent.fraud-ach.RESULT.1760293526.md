```json
{
  "id": "3451d6acb59dccd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293526,
  "host_pid": "9e6742732c60:1",
  "hash": "edb3800b0224f8630778a8453bd0e4e46c0a12b3fd6c41c4d73149deb4a855d7",
  "cid": "QmV1edb3800b0224f8630778a8453bd0e4e46c0a12b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293526,
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
      "evaluated_at": 1760293526
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
  "sig": "9b9fbe2761ec2b9ad9e2951d9c63769dd86550d4434b3e9a8f5460dc125f1b2f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596790322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 296, 'threshold': 50, 'total_amount': 15490864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 295, 'first_seen': 1760284979, 'matching_hash': 'b9497544c8340a37'}}}}