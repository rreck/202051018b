```json
{
  "id": "c80df29526be0712",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288051,
  "host_pid": "9e6742732c60:1",
  "hash": "29a7da611626deeffd1e28fdd6cc9e59bd96286847e084d00a95a2d3c36531c6",
  "cid": "QmV129a7da611626deeffd1e28fdd6cc9e59bd962868",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288051,
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
      "evaluated_at": 1760288051
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
  "sig": "ea443d46d2d0ac72b42b3b360581c8a0f033b962f57a20a9800dfde5cc7961d1"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 691661796885470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285764, 'matching_hash': 'c2d09785100b76ca'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}