```json
{
  "id": "a481a64287a1d8a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290838,
  "host_pid": "9e6742732c60:1",
  "hash": "f800d4c1ef85cb9e2b06ae367417ec8431cf4a4211a77b942039e8d7df4b22d7",
  "cid": "QmV1f800d4c1ef85cb9e2b06ae367417ec8431cf4a42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290838,
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
      "evaluated_at": 1760290838
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
  "sig": "e9f8b93303e6168468d9667f248a6af861e20dd812aff2fa279047e7f2df0035"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 699349871536240
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 59796000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285765, 'matching_hash': '372ab63252fc0966'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '699349873', 'validation_error': 'Invalid routing number checksum'}}}