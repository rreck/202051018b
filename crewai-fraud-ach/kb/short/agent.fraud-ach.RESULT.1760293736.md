```json
{
  "id": "106637c6138964be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293736,
  "host_pid": "9e6742732c60:1",
  "hash": "a98b63a94d22bebcb5c8b697033020b8debee16d2467a7b8db853a10da8f8f09",
  "cid": "QmV1a98b63a94d22bebcb5c8b697033020b8debee16d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293736,
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
      "evaluated_at": 1760293736
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
  "sig": "87f9a5fe477bdc679c91c98ed81c5d6a47b80135c269a13309fa123b0133dda4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466702370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 29947456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}