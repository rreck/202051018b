```json
{
  "id": "4c5070b16184409b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293086,
  "host_pid": "9e6742732c60:1",
  "hash": "11da63988bbd99941d5af823b2fc42277ebc1f9097d35a8a9b734a5056dab3eb",
  "cid": "QmV111da63988bbd99941d5af823b2fc42277ebc1f90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293086,
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
      "evaluated_at": 1760293086
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
  "sig": "6e709d39f11d64beb830cdeabb7a6f2902dfb16f9a5751569c545e4b0acbeba5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 000042122595756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 287, 'threshold': 50, 'total_amount': 113300712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 286, 'first_seen': 1760284979, 'matching_hash': 'f607cf2148e042a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '000042121', 'validation_error': 'Invalid routing number checksum'}}}