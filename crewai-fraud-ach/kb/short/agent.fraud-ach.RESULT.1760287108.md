```json
{
  "id": "8f0a30b154f46652",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287108,
  "host_pid": "9e6742732c60:1",
  "hash": "2348933f41a690b3c89658245877865c579545dba0cd4091a83b14b8a8176dd0",
  "cid": "QmV12348933f41a690b3c89658245877865c579545db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287108,
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
      "evaluated_at": 1760287108
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
  "sig": "60236f157aa24ac7cbd46e933420a5a35f75d46bde9f26f5e38158268f542788"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 107455396447712
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 23863584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285765, 'matching_hash': 'bb26c320d6c9a382'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '107455391', 'validation_error': 'Invalid routing number checksum'}}}