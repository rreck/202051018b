```json
{
  "id": "503a354a7dba0e1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293429,
  "host_pid": "9e6742732c60:1",
  "hash": "8eca715babeec942668054c981a00ce1616436af81190da75f7e2a7b861cc02d",
  "cid": "QmV18eca715babeec942668054c981a00ce1616436af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293429,
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
      "evaluated_at": 1760293429
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
  "sig": "cbfb64e019d33f27ce65eb29e0b170eae639f990ee6ac9567c68586553cf8e89"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 870312149939109
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 86994426, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': '2dbf2bb6cc4c52b4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}