```json
{
  "id": "a9ad67b2a9e8e897",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289053,
  "host_pid": "9e6742732c60:1",
  "hash": "5b51c30061c1c788aa3da19ddc26e19bf26d0ca5506bae42f336b14af620d82d",
  "cid": "QmV15b51c30061c1c788aa3da19ddc26e19bf26d0ca5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289053,
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
      "evaluated_at": 1760289053
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
  "sig": "85642536f3e14aa86050a3e88b4a7229a3d72d1ab3ce8dd6b6841c298e198553"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 498752223480159
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 44104816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '492624c5b9a9c8c0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}